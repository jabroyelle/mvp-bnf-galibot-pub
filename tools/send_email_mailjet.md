
# [send_email_mailjet.py](./send_email_mailjet.py)

Tool name: `send_email_mailjet`

Sends a test email using Mailjet SMTP.

## Prerequisites

You will need a [mailjet](https://www.mailjet.com/) account, and an [API key / Secret key](https://app.mailjet.com/account/apikeys).

Requires [email_mailjet](../connections/email_mailjet.yaml) connection with:
- MAILJET_APIKEY
- MAILJET_SECRETKEY
- FROM_EMAIL
- TO_EMAIL

You can create it with:
```sh
orchestrate connections import -f connections/email_mailjet_connection.yaml
```

Then populate it with:
```sh
orchestrate connections set-credentials --app-id email_mailjet --env draft \
    -e MAILJET_APIKEY=${MAILJET_APIKEY} \
    -e MAILJET_SECRETKEY=${MAILJET_SECRETKEY} \
    -e FROM_EMAIL=${FROM_EMAIL} \
    -e TO_EMAIL=${TO_EMAIL}
```

Note: you can also create a [.env.mailjet](../connections/.env.mailjet.sample) file and load it with the [create_connections script](../scripts/create_connections.sh)

Credentials are retrieved via [unified_connection_utils.py](./unified_connection_utils.py).

## Import

Import the tool, make sure you have the `--package-root tools` flag to import the `unified_connection_utils.py` library:

```sh
orchestrate tools import -k python -f ./tools/send_email_mailjet.py --package-root tools --app-id email_mailjet
```

## Test

You can check the tool in standalone with:
```sh
python ./tools/send_email_mailjet.py       
```