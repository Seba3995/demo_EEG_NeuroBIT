from pylsl import StreamInlet, resolve_stream
import matplotlib.pyplot as plt
import numpy as np

# Resolve any available stream
print("Looking for an available OpenSignals stream...")
streams = resolve_stream()

if not streams:
    print("No streams found.")
else:
    print(f"Found {len(streams)} stream(s).")
    for stream in streams:
        print(f"Stream name: {stream.name()}, type: {stream.type()}, hostname: {stream.hostname()}")

    # Connect to the first stream found
    inlet = StreamInlet(streams[0])
    print(f"Connected to stream: {inlet.info().name()}")

    # Configure chart
    plt.ion()
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    line, = ax.plot([], [], 'b-')
    plt.title("Real-Time EEG")
    plt.xlabel("Time (s)")
    plt.ylabel("EEG")
    window_size = 10000  # 10s
    ax.set_xlim(-window_size, 0)
    ax.set_ylim(0, 1000)
    ax.set_xticklabels([10, 8, 6, 4, 2, 0])

    # Main loop to update chart
    while True:
        samples = []
        timestamps = []

        # Get multiple samples at once
        for _ in range(1000):  # Adjustable according to performance
            sample, timestamp = inlet.pull_sample(timeout=0.0)
            if sample:
                samples.append(sample[1])  # channel used
                timestamps.append(timestamp)

        if samples:
            xdata = np.concatenate([xdata, np.arange(len(xdata), len(xdata) + len(samples))])
            ydata = np.concatenate([ydata, np.array(samples)])

            # Keep chart within the specified time window
            if len(ydata) > window_size:
                ydata = ydata[-window_size:]
                xdata = np.arange(-len(ydata), 0)

            # Adjustment - data from right to left
            line.set_xdata(np.array(xdata))
            line.set_ydata(np.array(ydata))
            ax.set_ylim(min(ydata) - 10, max(ydata) + 10)
            ax.set_xlim(-window_size, 0)
            plt.draw()
            plt.pause(0.01)
