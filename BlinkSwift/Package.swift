// swift-tools-version:3.1

import PackageDescription

let package = Package(
    name: "BlinkSwift",
    dependencies: [
        .Package(url: "https://github.com/uraimo/SwiftyGPIO.git", "1.0.7")
    ]
)
