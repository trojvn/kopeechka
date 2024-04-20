from kopeechka import KopeechkaMailWrapper


def main():
    kw = KopeechkaMailWrapper("18267d23b4cddae02146835673b80487")
    r = kw.reorder("tiktok.com", "esperfomin9554@mail.ru")
    print(r)
    r = kw.get_message(r)
    print(r)


if __name__ == "__main__":
    main()
