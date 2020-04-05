# Utility functions to crerate and verify QR codes
# Will be later integrated to django app with the
# API

import qrcode
from qrcode.image.pil import PilImage
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np

# Define the parameters for the QR code
# version : Integer from 1 to 40 that controls the size of the QR Code
# error_correction : parameter controls the error correction used for the QR Code.
# ERROR_CORRECT_L : 7%, M: 15%, Q : 25%, H: 30% or less
# Box Size : number of pixels for each box of the QR Code
# Border: How many boxes thick border should be

_VERSION = None
_ERROR_CORRECTION = qrcode.ERROR_CORRECT_L
_BOX_SIZE = 10
_BORDER = 4

# Functions for generating and verifying QR codes


def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=_VERSION,
        error_correction=_ERROR_CORRECTION,
        box_size=_BOX_SIZE,
        border=_BORDER
    )
    qr.add_data(
        text
    )
    qr.make(
        fit=True
    )
    image = qr.make_image(
        fill_color="black",
        back_color="white",
        image_factory=PilImage
    )
    image_np = np.array(image)
    return image_np


def decode_qr_code(image_np):
    pil_image = Image.fromarray(image_np)
    decoded_image = decode(pil_image)
    return decoded_image[0].data
