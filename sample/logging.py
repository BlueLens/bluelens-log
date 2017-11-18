from bluelens_log import Logging


options = {
  'REDIS_SERVER': "{YOUR_REDIS_SERVER_IP}",
  'REDIS_PASSWORD': "{YOUR_PASSWORD}"
}
log = Logging(options)

log.debug("debug log")
log.info("info log")
log.error("error log")
