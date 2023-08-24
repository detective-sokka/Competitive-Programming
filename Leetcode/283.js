// https://leetcode.com/problems/product-of-array-except-self/

var productExceptSelf = function(nums) {
    
    var total_product = 1
    var total_product_exc_zero = 1
    var num_zeroes = 0
    var result = new Array(nums.length).fill(0);

    for (var i=0; i < nums.length; i++) {

        total_product *= nums[i];
        
        if (nums[i] != 0) {
            
            total_product_exc_zero *= nums[i]
        
        } else {

            num_zeroes += 1
        }

        if (num_zeroes > 1) {
            
            return result;
        }

    }   

    for(var i=0; i < nums.length; i++) {

        if(nums[i] == 0) {
            
            result[i] = total_product_exc_zero;
            continue;
        }

        result[i] = total_product / nums[i];
    }
    
    return result;
};

console.log(productExceptSelf([0, 0]));