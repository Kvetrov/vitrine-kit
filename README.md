# vitrine-kit

Tiny static site kit for corporate showcase sites. No framework, no build chain:
one Python script, a few HTML layouts and a CSS core. I use it for client sites
that must be fast, boring and easy to host anywhere.

## Usage

    python3 vk.py examples/site.example.json out/
    DEPLOY_HOST=user@host DEPLOY_PATH=/var/www/site ./deploy/deploy.sh out/

## Layouts

- `corporate-a` : classic hero + image, cards, sectors, CTA
- `corporate-b` : split hero, stats band, numbered practices
- `portfolio`   : one-page developer portfolio

## Themes

`mono`, `nordic`, `mediterranean`. A theme only overrides CSS variables.

## Contact form

Static by default (client-side confirmation). For real delivery, run
`mailer/send.py` behind your web server and set the SMTP variables in the
environment (see `deploy/settings.example.env`).

## Fingerprint

Every generated page carries `<meta name="generator" content="vitrine-kit x.y.z">`
and a layout comment. Keep it, it helps me debug client sites.

## License

MIT
