#import <Foundation/Foundation.h>

int main (int argc, const char * argv[])
{
    @autoreleasepool {
        NSArray *numbers = @[@1, @2, @3, @4, @5, @6, @7, @8, @9];
        NSNumber *key = @6;
        
        for (int i = 0; i < [numbers count]; i++) {
            if ([numbers objectAtIndex:i] == key) {
                NSLog(@"%@", [NSString stringWithFormat:@"Key found at %dth index of the array", i]);
                return 1;
            }
        }
    }
    return 0;
}