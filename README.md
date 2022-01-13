# YANK

Personal terminal pastebin service. [Termbin](https://termbin.com/)
clone.

    alias yank="nc localhost 3000"

    echo "merhaba, ömürcan!" | yank
    http://localhost:3000/abcd

    cat file1.txt | yank
    http://localhost:3000/defg


To run the server just type this command:

    go run server.go


## REQUIREMENTS

- Golang
- and Golang.


## TODO

- [ ] create a config.toml to get host and port information.
- [ ] use basic auth for tcp connection.
- [ ] use logger instead of println.
- [ ] create a folder structure for keeping texts and serving them using nginx (or caddy?).
