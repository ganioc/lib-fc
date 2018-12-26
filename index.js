var fc = require('bindings')('fcapi.node');


module.exports = {
    sign_k1: fc.sign_compact,
    sign: fc.sign_compact
}
