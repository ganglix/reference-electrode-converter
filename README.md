# Electrode Potential Converter at 25°C

## Introduction
This Streamlit app is designed to assist researchers and students in converting potential readings between different reference electrodes at 25°C. It supports conversions among several standard reference electrodes including the Standard Hydrogen Electrode (SHE), Saturated Calomel Electrode (SCE), Copper-Copper(II) Sulfate Electrode (CSE), and the Silver-Silver Chloride (Ag/AgCl) electrode in saturated KCl. The app provides an intuitive interface for inputting potential values and selecting reference electrodes for conversion. Additionally, it features a visualization component that plots the reference electrode scales, illustrating the conversion result graphically.

## Setup
To run this app locally, you need Python and pip installed on your system. Follow these steps to set up the app:

1. Clone this repository to your local machine.
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the app's directory.
    ```bash
    cd electrode-potential-converter
    ```
3. Create a virtual environment.
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment.
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```
6. Run the app.
    ```bash
    streamlit run app.py
    ```

## Usage
After launching the app, follow these steps to perform a conversion:

1. Select the original reference electrode from the dropdown menu.
2. Enter the potential vs. the original reference electrode (in volts) in the provided input field.
3. Select the target reference electrode you want to convert the potential to.
4. Click the "Convert Potential" button to view the converted potential and visualize the reference electrode scales and the converted potential on the graph.

## Contributing
Contributions to improve the app are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
[MIT License](LICENSE)

