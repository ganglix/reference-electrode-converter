# Electrode Potential Converter

## Introduction
This Streamlit app enables users to convert electrode potential readings between different reference electrodes, accommodating temperature variations. It supports conversions among several standard reference electrodes including the Standard Hydrogen Electrode (SHE), Saturated Calomel Electrode (SCE), Copper-Copper(II) Sulfate Electrode (CSE), and the Silver-Silver Chloride (Ag/AgCl) electrode in saturated KCl. The app's intuitive interface allows users to input potential values, select reference electrodes, and specify operating temperatures for accurate conversion. A unique feature of this app is its ability to account for thermal effects on electrode potentials, offering both thermal and isothermal conversion options. Additionally, it features a visualization component that plots the reference electrode scales, illustrating the conversion result graphically.


## Webapp Link
https://reference-electrode-converter.streamlit.app

## Setup
To run this app locally, ensure you have Python and pip installed on your system. Follow these steps:

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
6. Launch the app.
    ```bash
    streamlit run app.py
    ```

## Usage
To use the app, perform the following steps:

1. Choose the "Select Temperature Dependence" option to indicate the conversion context—either Thermal or Isothermal.
2. Select the original reference electrode from the dropdown menu.
3. Input the potential vs. the original reference electrode (in volts).
4. Enter the operating temperatures for the original and target electrodes.
5. Select the target reference electrode for the conversion.
6. Click "Convert Potential" to obtain the converted potential. The visualization of reference electrode scales and the converted potential will be displayed on the graph, illustrating the impact of temperature adjustments.

## Contributing
Your contributions to enhance and improve the app are highly appreciated. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your enhancements (`git commit -am 'Add some enhancement'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a Pull Request.

## License
Distributed under the MIT License.
