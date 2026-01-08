import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def integrate_chunk(f, a, b, n_iter):
    h = (b - a) / n_iter
    result = 0.0
    for i in range(n_iter):
        result += f(a + i * h)
    return result * h


def parallel_integrate(f, a, b, n_iter, workers, executor_cls):
    step = (b - a) / workers
    n_per_worker = n_iter // workers

    tasks = []
    with executor_cls(max_workers=workers) as executor:
        for i in range(workers):
            start = a + i * step
            end = start + step
            tasks.append(
                executor.submit(integrate_chunk, f, start, end, n_per_worker)
            )

        result = sum(task.result() for task in tasks)

    return result


def measure(executor_cls):
    start = time.perf_counter()
    parallel_integrate(
        math.atan, 0, math.pi / 2,
        n_iter=10 ** 6,
        workers=4,
        executor_cls=executor_cls
    )
    return (time.perf_counter() - start) * 1000  # мс


if __name__ == "__main__":
    print("ThreadPool:", measure(ThreadPoolExecutor))
    print("ProcessPool:", measure(ProcessPoolExecutor))

