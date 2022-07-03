# YANK

Personal terminal pastebin service. [Termbin](https://termbin.com/)
clone.

```shell
# run server
$ yank server

# send text
$ yank url https://gokmengorgen.net
$ yank txt file1.txt
$ yank txt --secret  # opens your favourite editor.

# other operations
$ yank ls      # list
$ yank cp 2    # copy
$ yank rm 2    # remove

# configuration
$ yank config
```


## REQUIREMENTS

- Rust
- and Rust.


## TODO

- [ ] create a config.toml to get host and port information.
- [ ] use basic auth for tcp connection.
- [ ] use logger instead of println.
