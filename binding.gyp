{
    "targets": [
        {
            "target_name": "fcapi",
            "sources": [
                "src/fc-api.cpp",
            ],
            "include_dirs":[
                "<!(node -e \"require('nan')\")",
                "lib/secp256k1-zkp/include/",
                "/usr/local/include"
            ],
            "link_settings":{
                "libraries": [
                ],
                "ldflags":[
                ]
            },
            "conditions":[
                [
                    "OS=='mac'", {
                        "cflags!": ["-fno-exceptions"],
                        "cflags_cc!": [
                            "-O2",
                            "-std=gnu++14",
                            "-fno-exceptions",
                            "-Wall"
                        ],
                        "libraries":[
                            "-L<!(pwd)/lib/secp256k1-zkp/.libs "
                            "-L/usr/local/lib ",
                            "-lsecp256k1-zkp ",
                            "-lgmp "
                        ],
                        "xcode_settings":{
                            "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                            "GCC_ENABLE_CPP_RTTI": "YES",
                            "MACOSX_DEPLOYMENT_TARGET": '10.14',
                            "OTHER_CFLAGS": [
                                "-std=gnu++14",
                                "-stdlib=libc++"
                            ]
                        }
                    },
                    "OS=='linux'", {
                        "include_dirs": [
                            "/usr/include/arm-linux-gnueabihf"
                        ],
                        "cflags!": ["-fno-exceptions "],
                        "cflags_cc!": [
                            "-O2 ",
                            "-std=gnu++14 ",
                            "-fno-exceptions ",
                            "-Wall "
                        ],
                        "libraries":[
                            "-L<!(pwd)/lib/secp256k1-zkp/.libs "
                            "-L/usr/lib/arm-linux-gnueabihf ",
                            "-lsecp256k1-zkp ",
                            "-lgmp "
                        ]
                    }
                ]
            ]
        }
    ]
}
