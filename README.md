# Real-Time EEG Signal Acquisition Example with Neurobit and OpenSignals

This repo contains a Python code example for real-time EEG signal acquisition and visualization using the **Neurobit** device and the **Lab Streaming Layer (LSL)** library.

```signal_stream.py``` is based on the guide available for [BITalino and OpenSignals](https://bitalino.com/storage/uploads/media/open-signals-revolution---lab-streaming-layer-guide-python.pdf), adapted to work with Neurobit.

## Requirements
- **Python 3.7+**
- **pylsl**: Library for communication with LSL-compatible devices. [Documentation](https://github.com/labstreaminglayer/liblsl-Python)
- **Matplotlib**
- **NumPy**

You can install the necessary dependencies using pip:

```bash
pip install pylsl matplotlib numpy
