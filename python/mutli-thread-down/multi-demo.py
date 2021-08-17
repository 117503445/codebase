from htutil import file
import json

from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed


def init():
    lines = file.read_all_lines('urls.txt')
    dt_result = {}
    for line in lines:
        dt_result[line] = ''

    write_to_disk(dt_result)

    # exit()


def crawl_html(url: str) -> str:
    # if url == '100':
    #     raise Exception('error')
    return url + 'ok'


def write_to_disk(object):
    file.write_pkl('result.pkl', object)
    file.write_all_text('result.json', json.dumps(object, indent=4))


def main():
    init()

    dt_result: dict = file.read_pkl('result.pkl')
    no_crawled_urls = [k for k, v in dt_result.items() if len(v) == 0]

    task_pool = ThreadPoolExecutor(max_workers=128)
    future_to_url = {task_pool.submit(crawl_html, (url)): url
                     for url in no_crawled_urls}

    for index, future in enumerate(as_completed(future_to_url)):
        # if index % 100 == 0:
        #     write_to_disk(dt_result)
        url = future_to_url[future]
        try:
            data = future.result()
            dt_result[url] = data
        except Exception as ex:
            print(ex)
            # write_to_disk(dt_result)
            break

    write_to_disk(dt_result)


if __name__ == '__main__':
    main()
