# YANK

Personal terminal pastebin service. https://termbin.com/

    alias yank="nc localhost 3000"

    echo "merhaba, ömürcan!" | yank
    http://localhost:3000/abcd

    cat file1.txt | yank
    http://localhost:3000/defg


## REQUIREMENTS

- Golang
- and Golang.


## INSTALLATION

    sudo apt install fiche


## TODO

- [ ] create a config.toml to get host and port information.
- [ ] use basic auth for tcp connection.
- [ ] use logger instead of println.
- [ ] create a folder structure for keeping texts and serving them using nginx (or caddy?).
