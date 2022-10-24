#!/bin/bash

curl -X POST https://api.github.com/repos/yu-steven/openit/dispatches -H "Accept: application/vnd.github.everest-preview+json" -H "Authorization: token ${{ secrets.webhook }}" --data '{"event_type": "Webhook"}'
