import asyncio
import time

from request import some_tests

time_stamps = []


async def load_url(loop=None):
    future = loop.run_in_executor(None, some_tests)
    response = await future
    time_stamps.append(response)


def run_async():
    loop = asyncio.get_event_loop()
    task_list = [loop.create_task(load_url(loop=loop)) for _ in range(8)]

    start_time = time.time()
    loop.run_until_complete(asyncio.wait(task_list))
    wasted_time = time.time() - start_time
    loop.close()

    try:
        percentile = time_stamps[round(len(time_stamps) * 0.8) - 1]
        rps = round(len(time_stamps) / wasted_time)
    except:
        percentile, rps = None, None
    return percentile, rps, wasted_time


def test_rps():
    percentile, rps, wasted_time = run_async()
    if percentile:
        assert percentile < 0.450, f'Percentile too much: {percentile}, must be <0.450.' \
                                   f'\nAnswer times from server: {time_stamps}.\nWasted time on ' \
                                   f'all requests and responce: {wasted_time} '
        assert rps > 5, f'RPS should be <5, but actual: {rps}.' \
                        f'\nAnswer times from server: {time_stamps}.\nWasted time on ' \
                        f'all requests and responce: {wasted_time} '
    else:
        assert False, f'During operation there were incorrect responses from the server to requests.' \
                      f'\nAnswer times from server: {time_stamps}'
