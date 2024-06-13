import time
import requests
from datetime import datetime
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
CYAN = colorama.Fore.CYAN

now = datetime.now()
format = "%d/%m/%Y %H:%M:%S %p"
dt = now.strftime(format)

internal_urls = set()
external_urls = set()


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    urls = set()
    soup = BeautifulSoup(requests.get(url, allow_redirects=False).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                print(f"{GRAY}[!] {dt} External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{GREEN}[*] {dt} Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls


def crawl(url):

    print(f"\n{YELLOW}[*] {dt} Crawling: {url}{RESET}")

    t2_start = time.perf_counter()
    links = get_all_website_links(url)
    t2_stop = time.perf_counter()
    t2_to_crawl = t2_stop - t2_start

    print(
        f"{YELLOW}[*] {dt} Crawling End: {url} {RESET}{CYAN} << TIME TO CRAWL: {round(t2_to_crawl, 2)}(s) >>{RESET}\n"
    )

    for link in links:
        crawl(link)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("-u", "--url", help="The URL to extract links from.")

    args = parser.parse_args()
    url = args.url
    domain_name = urlparse(url).netloc

    t1_start = time.perf_counter()
    crawl(url)
    t1_stop = time.perf_counter()
    t1_to_crawl = t1_stop - t1_start

    print(f"\n\n\n{CYAN}>>>>>>>>>>>>>>>>>> Crawl Report <<<<<<<<<<<<<<<<<<{RESET}\n")
    print(f"{CYAN}[+] {dt} Total Internal links: {len(internal_urls)}{RESET}")
    print(f"{CYAN}[+] {dt} Total External links: {len(external_urls)}{RESET}")
    print(
        f"{CYAN}[+] {dt} Total URLs: {len(external_urls) + len(internal_urls)}{RESET}"
    )
    print(f"{CYAN}[+] {dt} Total Time to crawl: {round(t1_to_crawl, 2)}(s){RESET}")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n")

    # save the internal links to a file
    with open(f"{domain_name}_internal_links.txt", "w") as f:
        for internal_link in internal_urls:
            print(internal_link.strip(), file=f)

    # save the external links to a file
    with open(f"{domain_name}_external_links.txt", "w") as f:
        for external_link in external_urls:
            print(external_link.strip(), file=f)
