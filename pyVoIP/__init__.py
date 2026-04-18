__all__ = [
    "SIP", "RTP", "VoIP",
    "codec_support_report",
    "sip_supported_codecs",
    "supported_codecs",
]

from datetime import datetime, timezone

from pyVoIP._version import __version__, version_info

DEBUG = False

"""
The higher this variable is, the more often RTP packets are sent.
This should only ever need to be 0.0. However, when testing on Windows,
there has sometimes been jittering, setting this to 0.75 fixed this in testing.
"""
TRANSMIT_DELAY_REDUCTION = 0.0

"""
If registration fails this many times, VoIPPhone's status will be set to FAILED
and the phone will stop.
"""
REGISTER_FAILURE_THRESHOLD = 3


def debug(s, e=None):
    stamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    if DEBUG:
        print(f"[pyVoIP {stamp}] {s}")
    elif e is not None:
        print(f"[pyVoIP {stamp}] {e}")


# noqa because import will fail if debug is not defined
from pyVoIP.RTP import PayloadType  # noqa: E402

SIPCompatibleMethods = [
    "INVITE",
    "ACK",
    "BYE",
    "CANCEL",
    "OPTIONS",
    "SUBSCRIBE",
    "NOTIFY",
]
SIPCompatibleVersions = ["SIP/2.0"]

RTPCompatibleVersions = [2]
RTPCompatibleCodecs = [PayloadType.PCMU, PayloadType.PCMA, PayloadType.EVENT]


def supported_codecs():
    """Return codecs supported by this PyVoIP build/configuration."""
    from pyVoIP.RTP import supported_codecs as _supported_codecs

    return _supported_codecs()


def sip_supported_codecs(message, media_type="audio"):
    """Return codecs advertised by a parsed SIP message's SDP body."""
    from pyVoIP.SIP import sip_supported_codecs as _sip_supported_codecs

    return _sip_supported_codecs(message, media_type=media_type)


def codec_support_report(message, media_type="audio"):
    """Compare a SIP message's SDP codecs against PyVoIP support."""
    from pyVoIP.SIP import codec_support_report as _codec_support_report

    return _codec_support_report(message, media_type=media_type)
