#include <nan.h>
#include <node.h>
#include <node_buffer.h>
#include <iostream>

#include "secp256k1.h"

using namespace std;

const secp256k1_context_t *_get_context()
{
    static secp256k1_context_t *ctx = secp256k1_context_create(SECP256K1_CONTEXT_VERIFY | SECP256K1_CONTEXT_SIGN | SECP256K1_CONTEXT_RANGEPROOF | SECP256K1_CONTEXT_COMMIT);
    return ctx;
}

static int extended_nonce_function(unsigned char *nonce32, const unsigned char *msg32,
                                   const unsigned char *key32, unsigned int attempt,
                                   const void *data)
{
    unsigned int *extra = (unsigned int *)data;
    (*extra)++;
    return secp256k1_nonce_function_default(nonce32, msg32, key32, *extra, nullptr);
}

bool is_canonical(const unsigned char *c)
{
    return !(c[1] & 0x80) && !(c[1] == 0 && !(c[2] & 0x80)) && !(c[33] & 0x80) && !(c[33] == 0 && !(c[34] & 0x80));
}

void Print(const Nan::FunctionCallbackInfo<v8::Value> &info)
{
    if (!info[0]->IsString())
    {
    }

    // double n1 = 1.0;
    std::string str = "Hello everyone!";
    v8::Local<v8::String> output = Nan::New(str).ToLocalChecked();

    info.GetReturnValue().Set(output);
}
// Yang Jun
// in:  datahash in buffer, privatekey in buffer
// out: signature in buffer 65 bytes
//
void Sign_compact(const Nan::FunctionCallbackInfo<v8::Value> &info)
{
    if (info.Length() != 2)
    {
        Nan::ThrowTypeError("Wrong number of arguments, need 2");
        return;
    }
    // it's a Buffer or String
    // std::string str = *Nan::Utf8String(info[0]);
    v8::Local<v8::Object> sha256_buffer = info[0].As<v8::Object>();
    v8::Local<v8::Object> privKey32_buffer = info[1].As<v8::Object>();

    const unsigned char *sha256in = (const unsigned char *)node::Buffer::Data(sha256_buffer);
    // v8::Local<v8::Object> msg32_buffer = info[2].As<v8::Object>();

    const unsigned char *privKey32 = (const unsigned char *)node::Buffer::Data(privKey32_buffer);
    // unsigned char *input = (const unsigned char *)node::Buffer::Data(input_buffer);

    cout << "// input buffer" << endl;
    for (int i = 0; i < 32; i++)
    {
        cout << hex << (int)sha256in[i] << " ";
    }
    cout << endl;

    cout << "// private key" << endl;
    for (int i = 0; i < 32; i++)
    {
        cout << hex << (int)privKey32[i] << " ";
    }
    cout << "\n"
         << endl;

    unsigned char result[65];
    int recid;
    unsigned int counter = 0;
    int fb;

    do
    {
        fb = secp256k1_ecdsa_sign_compact(
            _get_context(),
            (unsigned char *)sha256in,
            (unsigned char *)&result[1],
            (unsigned char *)privKey32,
            extended_nonce_function,
            &counter,
            &recid);

        cout << "fb :" << fb << endl;
        cout << "recid :" << recid << endl;
    } while (!is_canonical(result));

    result[0] = 27 + 4 + recid;
    unsigned char output[65];

    cout << "Sign_compact signature result :" << endl;
    for (int i = 0; i < 65; i++)
    {
        output[i] = result[i];
        cout << hex << (int)output[i] << " ";
    }
    cout << "\n"
         << endl;

    info.GetReturnValue().Set(Nan::CopyBuffer((const char *)output, 65).ToLocalChecked());
}
void Init(v8::Local<v8::Object> exports)
{
    exports->Set(Nan::New("print").ToLocalChecked(),
                 Nan::New<v8::FunctionTemplate>(Print)->GetFunction());
    exports->Set(Nan::New("sign_compact").ToLocalChecked(),
                 Nan::New<v8::FunctionTemplate>(Sign_compact)->GetFunction());
}

NODE_MODULE(fcapi, Init)
