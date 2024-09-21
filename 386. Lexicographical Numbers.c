/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lexicalOrder(int n, int* returnSize) {
    int curr = 1;
    int* res = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        res[i] = curr;

        if (curr * 10 <= n)
            curr *= 10;
        else
        {
            while (curr % 10 == 9 || curr >= n)
                curr = (int) curr / 10;
            curr++;
        }
    }

    *returnSize = n;
    return res;
}