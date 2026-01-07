This integration was built for learning and experimentation, designed to be executed in a terminal environment.
You should create api_key from gemini and set to .env

Before running the project, ensure that all required dependencies are properly installed inside your virtual environment.

lib > gemini update sdk https://ai.google.dev/gemini-api/docs/migrate 
dependecy 
* pip install reportlab
* pip install weasyprint
* pip install -U -q "google-genai"
* pip install dotenv (if u set your API_KEY at .env) doc from gemini said to set at bashrc
* pip install markdown2

OBS: if u are using .venv 
Follow how to install and a alias to start-Deactive
python3 -m venv .venv

On "vim ~/.bashrc 
turn-off-venv() {
	if [ -d ".venv" ]; then
	  deactivate
	else
	  echo ".venv are not found in this dir"
	fi
}

turn-on-venv() {
  if [ -d ".venv" ]; then
    source .venv/bin/activate
  else
    echo ".venv are not found in this dir"
  fi
}
