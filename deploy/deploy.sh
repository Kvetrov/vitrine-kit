#!/bin/sh
# usage: DEPLOY_HOST=user@host DEPLOY_PATH=/var/www/site ./deploy/deploy.sh out/
set -e
[ -f deploy/settings.env ] && . deploy/settings.env
rsync -az --delete "${1:-out/}" "$DEPLOY_HOST:$DEPLOY_PATH/"
echo "deployed to $DEPLOY_HOST:$DEPLOY_PATH"
