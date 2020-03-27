# Wii U things
Forked from [ihaveamac/wiiu-things](https://github.com/ihaveamac/wiiu-things).
Using CETK (title.tik) creation from [giwty/FunKii-UI](https://github.com/giwty/FunKii-UI).

[FST format layout](https://github.com/ihaveamac/wiiu-things/wiki/FST)

* `wiiu_cdndownload.py` - Download titles from Nintendo CDN, including cetk (ticket). Generate cetk keys when extracted key is available.
* `wiiu_decrypt.py` - Decrypt titles from Nintendo CDN; requires Wii U Common Key, plus given encrypted titlekey if there is no cetk file.
* `wiiu_extract.py` - Extract contents from titles.
  * `--dump-info` - Print lots more info.
  * `--full-paths` - Show full paths in output.
  * `--no-extract` - Son't extract files, only show info.
  * `--all` - Show all files, including those with 0x80 bitmask in type (which probably means deleted file). only useful for title updates.
