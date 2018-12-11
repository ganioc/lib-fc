var fc = require('bindings')('fcapi.node');


module.exports = {
    sign_k1: fc.sign_k1,
    sign: fc.sign_k1
}
