# Secure Data Certificate Format Converter (SDCFC)

Secure Data Certificate Format Converter (SDCFC) is a powerful tool for managing certificate files, offering seamless conversion between PEM, DER, and PKCS12 formats. Whether you need to generate, convert, or manage certificates, SD-CFC provides a user-friendly interface to streamline your workflow securely.

## Features

- **Conversion**: Easily convert certificate files between PEM, DER, and PKCS12 formats.
- **Generation**: Generate self-signed certificates in PEM format.
- **Encryption**: Encrypt private keys with password protection.
- **User-Friendly**: Simple command-line interface for quick operations.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.
- Convert PEM to DER
- Convert DER to PEM
- Convert PEM to PKCS#12
- Convert PKCS#12 to PEM
- Convert DER to PKCS#12

## Installation

## Installation
To install SD-CFC, use pip:
```sh
pip install sdcfc

Usage
Command Line Interface

After installing, you can use the tool via command line:

sh

sdcfc

Example Usage

python

to i nvoke the mainmenu...
import sdcfc
# Now you can use functions or classes defined in sdfc module
sdcfc.main()

OR use you can specific functions as well

from sdcfc import PEMtoDERConverter, DERtoPEMConverter, PEMtoPKCS12Converter, PKCS12toPEMConverter, DERtoPKCS12Converter

# PEM to DER conversion
pem_to_der_converter = PEMtoDERConverter()
pem_to_der_converter.convert("path/to/certificate.pem", "path/to/certificate.der")

# DER to PEM conversion
der_to_pem_converter = DERtoPEMConverter()
der_to_pem_converter.convert("path/to/certificate.der", "path/to/certificate.pem")

# PEM to PKCS12 conversion
pem_to_pkcs12_converter = PEMtoPKCS12Converter()
pem_to_pkcs12_converter.convert("path/to/certificate.pem", "path/to/certificate.p12", password="your_password")

# PKCS12 to PEM conversion
pkcs12_to_pem_converter = PKCS12toPEMConverter()
pkcs12_to_pem_converter.convert("path/to/certificate.p12", "path/to/certificate.pem", password="your_password")

# DER to PKCS12 conversion
der_to_pkcs12_converter = DERtoPKCS12Converter()
der_to_pkcs12_converter.convert("path/to/certificate.der", "path/to/certificate.p12", password="your_password")

Menu Interface

Run the following command to start the interactive menu:

sh

sdcfc

You will be presented with a menu to choose the desired conversion.
Example Menu Usage

    Convert PEM to DER
    Convert DER to PEM
    Convert PEM to PKCS#12
    Convert PKCS#12 to PEM
    Convert DER to PKCS#12
    Exit

Connect with Me

    LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/
    GitHub: https://github.com/shubham10divakar
    Portfolio: https://shubham10divakar.github.io/showcasehub/

Feedback

Your feedback is important! Please share your thoughts and suggestions.
License

This project is licensed under the MIT License.