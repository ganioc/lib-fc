{
    "targets": [
        {
            "target_name": "fcapi",
            "sources": [
                "src/fc-api.cpp"
            ],
            "include_dirs":[
                "lib/fc/include/",
                "/usr/local/include",
                "<!(node -e \"require('nan')\")"
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
                        "cflags!": ["-fno-exceptions"],
                        "cflags_cc!": [
                            "-O2",
                            "-std=gnu++14",
                            "-fno-exceptions",
                            "-Wall"
                        ],
                        "libraries":[
                            "-L/Users/junyang/Documents/yangjun/project/gnuc/node-binding/test/lib/fc/build",
                            "-L/Users/junyang/Documents/yangjun/project/gnuc/node-binding/test/lib/fc/build/secp256k1",
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

                    }
                ]
            ]
        }
    ]
}
