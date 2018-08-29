# -*- coding: utf-8 -*-
import posixpath

from django.conf import settings
from django.core.files import File
from django.core.files.storage import DefaultStorage
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils._os import safe_join
from django.views.generic import RedirectView

from grandchallenge.challenges.models import Challenge
from grandchallenge.serving.api import serve_file
from grandchallenge.serving.permissions import can_access


def serve_folder(request, *, challenge_short_name=None, folder=None, path):
    """
    Serve static files in a folder.

    If the file is in a challenge folder, then the subfolders of this challenge
    will be checked for permissions, see `can_access`.

    If the challenge_short_name is not set, then the folder must be set.
    ALL FILES IN THIS FOLDER WILL BE AVAILABLE TO DOWNLOAD.
    """
    path = posixpath.normpath(path).lstrip("/")

    if challenge_short_name:
        if folder:
            raise AttributeError(
                "Only challenge_short_name or folder should be set"
            )
        challenge = get_object_or_404(
            Challenge, short_name__iexact=challenge_short_name
        )
        document_root = safe_join(settings.MEDIA_ROOT, challenge.short_name)
    elif folder:
        challenge = None
        document_root = safe_join(settings.MEDIA_ROOT, folder)
    else:
        raise AttributeError("challenge_short_name or folder must be set")

    fullpath = safe_join(document_root, path)

    if challenge:
        allowed = can_access(
            request.user,
            fullpath[len(document_root) :].lstrip("/"),
            challenge=challenge,
        )
    else:
        allowed = True

    storage = DefaultStorage()

    if storage.exists(fullpath) and allowed:
        try:
            f = storage.open(fullpath, "rb")
            file = File(f)
            return serve_file(file, save_as=True)
        except IOError:
            pass

    raise Http404("File not found.")


class ChallengeServeRedirect(RedirectView):
    # Do not redirect to a view name as this could skip some other handlers

    def get_redirect_url(self, *args, **kwargs):
        return f"/media/{kwargs['challenge_short_name']}/{kwargs['path']}/"