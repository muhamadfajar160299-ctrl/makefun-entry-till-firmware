# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/muhamadfajar160299-ctrl/makefun-entry-till-firmware/rank.svg)](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/muhamadfajar160299-ctrl/makefun-entry-till-firmware/reward.svg)](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929)

An entry for the [Till Firmware Do Us Part](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929) competition on make.fun: one original single-sentence wedding vow spoken by a robot at its own wedding — funny and heartfelt at once, in a machine's own voice, kept under 200 characters so every word earns its place.

## How it works

`main.py` (Python standard library only, no network) copies the shipped vow in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — referral `gt86z8ct`.
