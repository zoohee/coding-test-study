// return String
var input = readLine()!

// return Int
var input = Int(readLine()!)!

// =========================================

// split - return: [SubString] 
var nums = readLine()!.split(separator: " ").map {Int($0)!} 

// components - return: [String] -> import Foundation 필수
var nums = readLine()!.components(separatedBy: " ").map {Int($0)!}

// FileIO, 입력받으면서 리스트에 바로 추가하기
array.append((file.readInt(), file.readInt()))

// =========================================

// Int
var nums = Array(readLine()!).map {Int(String($0))!}

// String
var nums = Array(readLine()!).map {String($0)}

// FileIO
let nums = [file.readInt(), file.readInt()]

let strData = "hello성훈!!"

// =========================================

// [prefix : 시작 기준으로 지정한 문자 개수 출력]
let startData = strData.prefix(5)
print(startData)  // hello

// [suffix : 종료 기준으로 지정한 문자 개수 출력]
let endData = strData.suffix(4)
print(endData) // 성훈!!

// =========================================

let numbers = [1, 2, 3, 4, 5]
print(numbers.prefix(2))
// Prints "[1, 2]"
print(numbers.prefix(10))
// Prints "[1, 2, 3, 4, 5]"

let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"

// =========================================

/// 기준이 되는 문자를 제외한 요소를 배열로 만들어 리턴
let dartResult = "1S2D*3T"
var scores = dartResult.split(whereSeparator: {!$0.isNumber}).map {Int($0)!}
print(scores)
// Prints "[1, 2, 3]"
let letters = dartResult.split(whereSeparator: {$0.isNumber})
print(letters)
// Prints "["S", "D*", "T"]"


// =========================================

// 3번째부터 끝까지
let startIdx: String.Index = str.index(str.startIndex, offsetBy: 3)
var result = String(str[startIdx...])

// 처음부터 3번째까지
let endIdx: String.Index = str.index(str.startIndex, offsetBy: 3)
var result = String(str[...endIdx])


// =========================================

let str = String(repeating: "ㅋ", count: 10)
print(str) // "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"

// import Foundation 필수
let str = "ung!chun!"
let str2 = str.replacingOccurrences(of: "!", with: "?")
print(str2) // ung?chun?

print("Hello", terminator:"")

// =========================================

let nums: [Int] = [1, 2, 3, 4]

nums.forEach {
	print($0) // 1 2 3 4
}