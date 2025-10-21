def fifo_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    print("Page Reference String:", pages)
    print("Frame Size:", frame_size)
    print("\nPage\tFrames\t\t\tPage Fault")
    print("--------------------------------------------")

    for page in pages:
        if page not in frames:
            page_fault = "Miss"
            page_faults += 1
            if len(frames) == frame_size:
                frames.pop(0)
            frames.append(page)
        else:
            page_fault = "Hit"

        if len(frames) < 3:
            print(f"{page}\t{frames}\t\t\t{page_fault}")
        else:
            print(f"{page}\t{frames}\t\t{page_fault}")

    print("\nTotal Page Faults:", page_faults)


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
frame_size = 3

fifo_page_replacement(pages, frame_size)
