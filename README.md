# Galibot - BNF & IBM

DESCRIPTION

## Architecture

## Initial setup

Prequisites : 
- Installed Orchestrate ADK on machine

1. Environment variables :
    - Create a `.env`file. You can start from scratch or copy and rename .env.example, for example : `cp .env.example .env`
    ```
    WO_DEVELOPER_EDITION_SOURCE=orchestrate
    WO_API_KEY=
    WO_INSTANCE=
    AUTHORIZATION_URL=https://iam.platform.saas.ibm.com/siusermgr/api/1.0/apikeys/token

    DOCKER_CLIENT_TIMEOUT=2000
    COMPOSE_HTTP_TIMEOUT=2000
    HEALTH_TIMEOUT=2000
    ```
    - WO_API_KEY : follow this tutorial [https://developer.watson-orchestrate.ibm.com/environment/production_import#ibm-cloud]
    - WO_INSTANCE : looks something like this [https://api.us-south.watson-orchestrate.cloud.ibm.com/instances/xxxx]

2. Load all agents and knowledge base : 

```bash
orchestrate server start -l --env-file .env
orchestrate env activate local

orchestrate knowledge-bases import -f knowledge_base/essentials_data.yaml
orchestrate knowledge-bases import -f knowledge_base/exhibition_data.yaml
orchestrate knowledge-bases import -f knowledge_base/galica_data.yaml

orchestrate agents import -f agents/BNF_librarian_agent.yaml
orchestrate agents import -f agents/Documentalist_agent.yaml
orchestrate agents import -f agents/Exhibition_agent.yaml
orchestrate agents import -f agents/galibo_agent.yaml
```

## Run the app

```bash
orchestrate chat start
```


Open the application [http://localhost:3000/](http://localhost:3000/)

## Start the crawler

```bash
# Initial setup
python -m venv .venv   
source ./.venv/bin/activate
python -m pip install requests
python -m pip install beautifulsoup4
python -m pip install selenium

# Run the code
python crawler_litterature.py   
python crawler_expositions.py   
```

## [draft} Extract info from epub

```bash
python -m venv .venv   
source ./.venv/bin/activate
pip install epub2pdf

# Run the code
python crawler_expositions.py
```

## Backend

```bash
python -m venv venv
source venv/bin/activate 

cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

[Application](http://127.0.0.1:8000/docs)


Push to registry 

``` bash
ibmcloud login --sso
ibmcloud plugin install container-registry -r 'IBM Cloud'
ibmcloud cr login --client docker

docker build --platform linux/amd64 -t fastapi-reservation .
docker tag fastapi-reservation de.icr.io/cc-310002m8rk-8g50u0vv-cr/galibot-backend:1.0   
docker push  de.icr.io/cc-310002m8rk-8g50u0vv-cr/galibot-backend:1.0 
```

## Embed chat in a website

Here is a quick way to embed the orchestrate chat in a external website without having to develop anything.

1. All orchestrate environment come with embed security enabled by default. You either want to configure your environment to be secure or to be accessible to anyone without login. To do so, follow this [documentation](https://developer.watson-orchestrate.ibm.com/agents/integrate_agents#enabling-security)
    1. Create a `wxO-embed-chat-security-tool.sh` file on your computer
    2. Paste the content of the script in the file than save
    3. On Unix-based systems (macOS and Linux), change the permissions to run the script: `chmod +x wxO-embed-chat-security-tool.sh`
    4. Run the script `./wxO-embed-chat-security-tool.sh` and follow prompts to enable or disable the security. For this project, as our the embedding is temporary and disappears when we reload the page, we disabled security.

2. Go to Watsonx Orchestrate interface
3. Open the menu -> Build -> Agent builder
4. Click on your master agent
5. In the side navigation, click on "Channels"
6. Click on "Embedded agent" -> "Live"
7. Copy the script 
8. Go to your client website, in our case [https://www.bnf.fr/fr](https://www.bnf.fr/fr)
9. Open the console
10. Paste the code without script and tap on enter on your keyboard. It should look like this :
```js
  window.wxOConfiguration = {
    orchestrationID: "xxxxxx",
    hostURL: "https://us-south.watson-orchestrate.cloud.ibm.com",
    rootElementID: "root",
    deploymentPlatform: "ibmcloud",
    crn: "crn:v1:bluemix:public:watsonx-orchestrate:us-south:a/xxxxxx::",
    chatOptions: {
        agentId: "xxxx", 
        agentEnvironmentId: "xxxxx",
    }
  };
  setTimeout(function () {
    const script = document.createElement('script');
    script.src = `${window.wxOConfiguration.hostURL}/wxochat/wxoLoader.js?embed=true`;
    script.addEventListener('load', function () {
        wxoLoader.init();
    });
    document.head.appendChild(script);
  }, 0);                     
```
11. Click on the newly appeared blue chat bubble in the bottom right corner of you page
12. Play out your scenario



