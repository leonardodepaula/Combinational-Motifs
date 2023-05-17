class NSNodeMixin:

    def get_descendants(self, include_self=False):
        if include_self == False:
            if self.is_leaf():
                return self.get_result_class(self.__class__).objects.none()
            else:
                return self.__class__.get_tree(self).exclude(pk=self.pk)
        else:
            return self.__class__.get_tree(self)

def get_ancestors(self, include_self=False):

    if include_self == False:
        if self.is_root():
            return self.get_result_class(self.__class__).objects.none()
        else:
            return self.get_result_class(self.__class__).objects.filter(
                tree_id=self.tree_id,
                lft__lt=self.lft,
                rgt__gt=self.rgt)
    else:
        if self.is_root():
            return self.get_result_class(self.__class__).objects.filter(
                tree_id=self.tree_id,
                depth=1)
        else:
            return self.get_result_class(self.__class__).objects.filter(
                tree_id=self.tree_id,
                lft__lte=self.lft,
                rgt__gte=self.rgt)