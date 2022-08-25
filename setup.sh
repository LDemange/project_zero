mkdir -p ~/.streamlit/

echo "\n\
[general]\n\
email = \"demange.louis@hotmail.fr\"\n\
" >> ~/.streamlit/credentials.toml

echo "\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" >> ~/.streamlit/config.toml
