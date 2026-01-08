from concurrent.futures import ThreadPoolExecutor

def write_file():
    with open("data.txt", "w") as f:
        f.write("Макларен спасибо за кубок конструкторов в 2024 и 2025 годах!")
    return "written"


def read_file():
    with open("data.txt", "r") as f:
        return f.read()


with ThreadPoolExecutor(max_workers=2) as executor:
    future_write = executor.submit(write_file)
    future_write.result()
    future_read = executor.submit(read_file)

    print("Прочитано:", future_read.result())