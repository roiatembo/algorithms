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

  console.log(twoSum([1,2,5,5,11], 10))