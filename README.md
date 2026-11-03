# hello-cog

A tiny Cog model. Every push to `main` builds the image on GitHub Actions and
publishes it to `ghcr.io/<owner>/<repo>:latest`.

Test locally (optional, needs Docker): `cog run -i name=Moh -i repeat=2`
