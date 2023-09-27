#import <Foundation/Foundation.h>

NSInteger binarySearch(NSArray *array, NSInteger target) {
    NSInteger left = 0;
    NSInteger right = [array count] - 1;

    while (left <= right) {
        NSInteger mid = left + (right - left) / 2;
        NSInteger midValue = [array[mid] integerValue];

        if (midValue == target) {
            return mid; 
        } else if (midValue < target) {
            left = mid + 1; 
        } else {
            right = mid - 1;
        }
    }

    return -1; 
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSArray *sortedArray = @[@1, @3, @5, @7, @9, @11, @13];
        NSInteger target = 7;
        NSInteger result = binarySearch(sortedArray, target);

        if (result != -1) {
            NSLog(@"Element %ld found at index %ld", (long)target, (long)result);
        } else {
            NSLog(@"Element %ld not found in the array", (long)target);
        }
    }
    return 0;
}
