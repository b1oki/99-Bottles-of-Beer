# 99 Bottles of Beer

[![GitHub release](https://img.shields.io/github/release/b1oki/99-Bottles-of-Beer?maxAge=2592000&style=for-the-badge)](https://github.com/b1oki/99-Bottles-of-Beer)
[![GitHub license](https://img.shields.io/github/license/b1oki/99-Bottles-of-Beer?style=for-the-badge)](https://github.com/b1oki/99-Bottles-of-Beer)
 
## Translation

### Generation
 
`xgettext -j -s -d bottles -o bottles/locales/ru/LC_MESSAGES/bottles.po bottles/bottles.py`

### Compilation

`msgfmt -o bottles/locales/ru/LC_MESSAGES/bottles.mo bottles/locales/ru/LC_MESSAGES/bottles`
