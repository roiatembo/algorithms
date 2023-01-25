// my solution with a time complexity of O(n*n)

var twoSum = function(nums, target) {
    const targetArray = []
      for (let i=0; i<nums.length; i++) {
          for(let j=1+i; j<nums.length; j++) {
              if ((nums[i] + nums[j]) == target) {
                  targetArray.push(i)
                  targetArray.push(j)
                  return targetArray
               }
          }
      }
  };

// lectures solution with a time complexity of O(n) and space complexity of O(n)

function twoIndices(nums, target) {
    hashTable = {}
    for (let i=0; i < nums.length; i++) {
        var needed = target - nums[i]
        if (needed in hashTable) {
            return[i, hashTable[needed]]
        } else {
            hashTable[nums[i]] = i
        }
    }
    return [];
}


  arr = [2,7,3,-1,4]
  target = 2
  console.log(twoSum(arr, target))
  console.log(twoIndices(arr, target))