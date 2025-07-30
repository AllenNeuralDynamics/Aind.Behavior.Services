namespace AindBehaviorServices.MessageProtocol
{
    public partial class MatchRegisteredPayload
    {
        private static System.IObservable<TResult> Process<TResult>(System.IObservable<object> source)
            where TResult : RegisteredPayload
        {
            return System.Reactive.Linq.Observable.Create<TResult>(observer =>
            {
                var sourceObserver = System.Reactive.Observer.Create<object>(
                    value =>
                    {
                        var match = value as TResult;
                        if (match != null) observer.OnNext(match);
                    },
                    observer.OnError,
                    observer.OnCompleted);
                return System.ObservableExtensions.SubscribeSafe(source, sourceObserver);
            });
        }
    }
}
