{
    "targets": [
        {
            "target_name": "fcapi",
            "sources": [
                "src/fc-api.cpp"
            ],

            "link_settings":{
                "libraries": [
                    "-lfc"
                ],
                "ldflags":[
                ]
            },
            "conditions":[
                [
                    "OS=='mac'", {
                        "include_dirs": [
                            "lib/fc/include/",
                            "/usr/local/include",
                            "<!(node -e \"require('nan')\")"
                        ],
                        "cflags!": ["-fno-exceptions"],
                        "cflags_cc!": [
                            "-O2",
                            "-std=gnu++14",
                            "-fno-exceptions",
                            "-Wall"
                        ],
                        "libraries":[
                            "-L<!(pwd)/lib/fc/build",
                            "-L<!(pwd)/lib/fc/build/secp256k1",
                            "-L/usr/local/lib",
                            "-lfc",
                            "-lsecp256k1",
                            "-lboost_chrono-mt",
                            "-lboost_date_time-mt",
                            "-lboost_filesystem-mt",
                            "-lboost_system-mt",
                            "-lboost_unit_test_framework-mt",
                            "-lgmp"
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
                            "lib/fc/include/",
                            "/usr/include",
                            "/usr/local/ssl/include",
                            "<!(node -e \"require('nan')\")"
                        ],
                        "cflags!": ["-fno-exceptions"],
                        "cflags_cc!": [
                            "-O2",
                            "-std=c++14",
                            "-fno-exceptions",
                            "-Wall"
                        ],
                        "libraries":[
                            "-L<!(pwd)/lib/fc/build",
                            "-L<!(pwd)/lib/fc/build/secp256k1",
                            "-L/usr/local/lib",
                            "-L/usr/local/ssl/lib",
                            "-L/usr/lib/x86_64-linux-gnu",
                            "-lfc",
                            "-lsecp256k1",
                            "-lboost_chrono-mt",
                            "-lboost_date_time-mt",
                            "-lboost_filesystem-mt",
                            "-lboost_system-mt",
                            "-lboost_unit_test_framework-mt",
                            "-lgmp"
                        ]
                    }
                ]
            ]
        }
    ]
}
