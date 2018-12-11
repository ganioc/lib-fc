#include <nan.h>
#include <iostream>

#include <fc/crypto/public_key.hpp>
#include <fc/crypto/private_key.hpp>
#include <fc/crypto/signature.hpp>
#include <fc/utility.hpp>

using namespace std;
using namespace fc;
using namespace fc::crypto;

/**
 * Input :
 *  info[0] : data( Buffer )
 *  info[1] : private key ( string )
 * 
 *  output : signature 
 */
void Sign_k1(const Nan::FunctionCallbackInfo<v8::Value> &info)
{
  if (info.Length() != 2)
  {
    Nan::ThrowTypeError("Wrong number of arguments, need 2");
    return;
  }
  // else
  // {
  //   cout << "<< "
  //        << "Arguments length is 2" << endl;
  // }
  // Judge if info[1] is a string?
  if (!info[1]->IsString())
  {
    Nan::ThrowTypeError("Wrong arguments types, should be string");
    return;
  }
  std::string inPrivate = *Nan::Utf8String(info[1]);
  auto privateKey = private_key(inPrivate);

  fc::sha256 digest;

  // it's a Buffer or String

  std::string str = *Nan::Utf8String(info[0]);

  digest = fc::sha256::hash(str);

  cout << "<< " << std::string(digest) << endl;

  auto sig = privateKey.sign(digest, true);

  v8::Local<v8::String> output = Nan::New(std::string(sig)).ToLocalChecked();

  info.GetReturnValue().Set(output);
}
void Init(v8::Local<v8::Object> exports)
{

  exports->Set(Nan::New("sign_k1").ToLocalChecked(),
               Nan::New<v8::FunctionTemplate>(Sign_k1)->GetFunction());
}

NODE_MODULE(fcapi, Init)
