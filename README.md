# Wii U things
Taking basic stuff from [ihaveamac/wiiu-things](https://github.com/ihaveamac/wiiu-things) and CETK (title.tik) creation from [giwty/FunKii-UI](https://github.com/giwty/FunKii-UI).

[FST format layout](https://github.com/ihaveamac/wiiu-things/wiki/FST)

* `wiiu_cdndownload.py` - Download titles from Nintendo CDN, including cetk (ticket). Generate CETK keys when extracted key is available.
* `wiiu_decrypt.py` - Decrypt titles from Nintendo CDN; requires Wii U Common Key, plus given encrypted titlekey if there is no CETK file.
* `wiiu_extract.py` - Extract contents from titles.
  * `--dump-info` - Print lots more info.
  * `--full-paths` - Show full paths in output.
  * `--no-extract` - Don't extract files, only show info.
  * `--all` - Show all files, including those with 0x80 bitmask in type (which probably means deleted file). only useful for title updates.
* `wiiu_titlekeys.py` - Generate a formatted JSON file with all the known keys.
  * `--cemu` - Generates a text key list for use with CEMU.
