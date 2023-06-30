/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    const a = nums.length
    for(let i = 0; i < a; i++) {
        nums.push(nums[i])
    }
    return nums
};