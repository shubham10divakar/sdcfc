# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:00:52 2024

@author: Subham Divakar
"""

# main.py
from converters.pem_to_der import PEMtoDERConverter
from converters.der_to_pem import DERtoPEMConverter
from converters.pem_to_pkcs12 import PEMtoPKCS12Converter
from converters.pkcs12_to_pem import PKCS12toPEMConverter
from converters.der_to_pkcs12 import DERtoPKCS12Converter

def main():
    print("Welcome to the Secure Data Certificate Format Converter (SD-CFC)!")
    print("SD-CFC is a powerful tool for managing certificate files.")
    print("It offers seamless conversion between PEM, DER, and PKCS12 formats.")
    print("Whether you need to convert, or manage certificates,")
    print("SD-CFC provides a user-friendly interface to streamline your workflow securely.")

    print("This tool converts certs from one format(PEM, DER, PKCS12) files to other formats(PEM, DER, PKCS12).\n")
    
    print("Created by Subham Divakar\n")
    print("Connect with me:")
    print("- LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/")
    print("- GitHub: https://github.com/shubham10divakar")
    print("- Portfolio: https://shubham10divakar.github.io/showcasehub/")
    print("\n")
    
    print("1. Convert PEM to DER")
    print("2. Convert DER to PEM")
    print("3. Convert PEM to PKCS#12")
    print("4. Convert PKCS#12 to PEM")
    print("5. Convert DER to PKCS#12")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        pem_filename = input("Enter the PEM filename (without extension): ").strip() + ".pem"
        der_filename = input("Enter the DER filename to save (without extension): ").strip() + ".der"
        converter = PEMtoDERConverter()
        converter.convert(pem_filename, der_filename)
        print(f"Conversion from PEM to DER complete. Output saved to {der_filename}.")
    elif choice == '2':
        der_filename = input("Enter the DER filename (without extension): ").strip() + ".der"
        pem_filename = input("Enter the PEM filename to save (without extension): ").strip() + ".pem"
        converter = DERtoPEMConverter()
        converter.convert(der_filename, pem_filename)
        print(f"Conversion from DER to PEM complete. Output saved to {pem_filename}.")
    elif choice == '3':
        pem_filename = input("Enter the PEM filename (without extension): ").strip() + ".pem"
        pkcs12_filename = input("Enter the PKCS#12 filename to save (without extension): ").strip() + ".pfx"
        password = input("Enter password for PKCS#12 (leave blank for no encryption): ").strip()
        converter = PEMtoPKCS12Converter()
        converter.convert(pem_filename, pkcs12_filename, password)
        print(f"Conversion from PEM to PKCS#12 complete. Output saved to {pkcs12_filename}.")
    elif choice == '4':
        pkcs12_filename = input("Enter the PKCS#12 filename (without extension): ").strip() + ".pfx"
        pem_filename = input("Enter the PEM filename to save (without extension): ").strip() + ".pem"
        password = input("Enter password for PKCS#12 (leave blank if not encrypted): ").strip()
        converter = PKCS12toPEMConverter()
        converter.convert(pkcs12_filename, pem_filename, password)
        print(f"Conversion from PKCS#12 to PEM complete. Output saved to {pem_filename}.")
    elif choice == '5':
        der_filename = input("Enter the DER filename (without extension): ").strip() + ".der"
        pkcs12_filename = input("Enter the PKCS#12 filename to save (without extension): ").strip() + ".pfx"
        password = input("Enter password for PKCS#12 (leave blank for no encryption): ").strip()
        converter = DERtoPKCS12Converter()
        converter.convert(der_filename, pkcs12_filename, password)
        print(f"Conversion from DER to PKCS#12 complete. Output saved to {pkcs12_filename}.")
    elif choice == '6':
        print("Exiting (SD-CFC) === Secure Data Certificate Format Converter Tool ===\n")
        print("Feedbacks are welcome.\n")
        print("Created by Subham Divakar\n")
        print("Connect with me:")
        print("- LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/")
        print("- GitHub: https://github.com/shubham10divakar")
        print("- Portfolio: https://shubham10divakar.github.io/showcasehub/")
        print("\n")
    else:
        print("Invalid choice. Please enter a number between 1 and 5")


if __name__ == "__main__":
    main()