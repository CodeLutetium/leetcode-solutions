typedef struct {
    int val;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct {
    int size;
    int capacity;
    Node* first;
    Node* last;
} MyCircularDeque;

MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque* deque = malloc(sizeof(MyCircularDeque));
    deque->size = 0;
    deque->capacity = k;
    deque->first = NULL;
    deque->last = NULL;
    return deque;
}

bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if (obj->size == obj->capacity)
        return false;

    Node* node = malloc(sizeof(Node));
    node->val = value;
    node->prev = NULL;
    node->next = obj->first;

    if (obj->size > 0) 
    {
        obj->first->prev = node;
    }
    else
    {
        obj->last = node;
    }

    obj->first = node;
    obj->size++;
    return true;
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if (obj->size == obj->capacity)
        return false;

    Node* node = malloc(sizeof(Node));
    node->val = value;
    node->next = NULL;
    node->prev = obj->last;

    if (obj->size > 0) 
    {
        obj->last->next = node;
    }
    else
    {
        obj->first = node;
    }

    obj->last = node;
    obj->size++;
    return true;
}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if (obj->size == 0)
        return false;

    obj->first = obj->first->next;

    if (obj->size > 1) 
    {
        obj->first->prev = NULL;
    }
    else
    {
        obj->last = obj->first;
    }
    obj->size--;

    return true;
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if (obj->size == 0)
        return false;

    obj->last = obj->last->prev;

    if (obj->size > 1)
    {
        obj->last->next = NULL;
    }
    else
    {
        obj->first = obj->last;
    }
    obj->size--;

    return true;
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if (obj->size > 0)
        return obj->first->val;

    return -1;
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if (obj->size > 0)
        return obj->last->val;

    return -1;
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    return obj->size == 0;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    return obj->size == obj->capacity;
}

void myCircularDequeFree(MyCircularDeque* obj) {
    Node* curr = obj->first;

    while (curr)
    {
        Node* next = curr->next;
        free(curr);
        curr = next;
    }
    free(obj);
}

/**
 * Your MyCircularDeque struct will be instantiated and called as such:
 * MyCircularDeque* obj = myCircularDequeCreate(k);
 * bool param_1 = myCircularDequeInsertFront(obj, value);

 * bool param_2 = myCircularDequeInsertLast(obj, value);

 * bool param_3 = myCircularDequeDeleteFront(obj);

 * bool param_4 = myCircularDequeDeleteLast(obj);

 * int param_5 = myCircularDequeGetFront(obj);

 * int param_6 = myCircularDequeGetRear(obj);

 * bool param_7 = myCircularDequeIsEmpty(obj);

 * bool param_8 = myCircularDequeIsFull(obj);

 * myCircularDequeFree(obj);
*/