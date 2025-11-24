MAILJET_APIKEY=b2f581eaf1f89bba584b5e3d7f8c4a77
MAILJET_SECRETKEY=817866328f034dfaf352922dc3b8a763
FROM_EMAIL=jabroyelle@gmail.com
TO_EMAIL=jd5224336@gmail.com


orchestrate connections set-credentials --app-id email_mailjet --env draft \
    -e MAILJET_APIKEY=${MAILJET_APIKEY} \
    -e MAILJET_SECRETKEY=${MAILJET_SECRETKEY} \
    -e FROM_EMAIL=${FROM_EMAIL} \
    -e TO_EMAIL=${TO_EMAIL}
