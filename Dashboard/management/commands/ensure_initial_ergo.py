"""
Bootstrap the first ergotherapist when no Shell access is available (e.g. Render free tier).

Set env var INITIAL_ERGO_PASSWORD (and optionally others), deploy once, then remove the
password from environment variables after first login.
"""

import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Creates first ergotherapist user from INITIAL_ERGO_* environment variables."

    def handle(self, *args, **options):
        password = (os.environ.get("INITIAL_ERGO_PASSWORD") or "").strip()
        if not password:
            self.stdout.write(
                self.style.WARNING(
                    "ensure_initial_ergo: INITIAL_ERGO_PASSWORD not set — skipping "
                    "(this is normal if you create users another way)."
                )
            )
            return

        username = (os.environ.get("INITIAL_ERGO_USERNAME") or "admin").strip()
        email = (os.environ.get("INITIAL_ERGO_EMAIL") or "").strip()
        nom = (os.environ.get("INITIAL_ERGO_NOM") or "Cabinet").strip()
        prenom = (os.environ.get("INITIAL_ERGO_PRENOM") or "Admin").strip()

        if not username:
            self.stderr.write(self.style.ERROR("ensure_initial_ergo: INITIAL_ERGO_USERNAME empty."))
            raise SystemExit(1)

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f"ensure_initial_ergo: user {username!r} already exists — skipping."
                )
            )
            return

        if not email:
            email = f"{username}@initial.local"

        base_suffix = 0
        candidate = email
        while User.objects.filter(email__iexact=candidate).exists():
            base_suffix += 1
            candidate = f"{username}+{base_suffix}@initial.local"
        email = candidate

        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                nom=nom,
                prenom=prenom,
                role="ergo",
                code="-",
            )
        except Exception as exc:
            self.stderr.write(self.style.ERROR(f"ensure_initial_ergo: failed: {exc}"))
            raise SystemExit(1) from exc

        self.stdout.write(
            self.style.SUCCESS(
                f"ensure_initial_ergo: created ergotherapist login username={username!r}. "
                "Remove INITIAL_ERGO_PASSWORD from your host env after first login."
            )
        )
